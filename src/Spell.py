from dataclasses import dataclass, field


@dataclass
class Spell:
    """
    Spell class controls spell duration and counts how many spells are used.
    It also handles gem-vs-gem combat logic.
    """
    _seconds: float = field(init=False, default=1.0)
    _spell_count: int = field(init=False, default=0)

    # -------------------------
    # Spell counter
    # -------------------------

    def increase_spell_count(self, amount: int = 1) -> None:
        """
        Increases the number of spells used.
        This value is used to calculate remaining oxygen.
        """
        self._spell_count += amount

    @property
    def counter(self) -> int:
        """
        Returns the number of spells used.
        """
        return self._spell_count

    # -------------------------
    # Spell duration
    # -------------------------

    @property
    def duration(self) -> float:
        """
        Returns the duration of the spell in seconds.
        """
        return self._seconds

    @duration.setter
    def duration(self, value: float) -> None:
        """
        Sets spell duration.
        Must be >= 1.0 seconds.
        """
        self._seconds = value if value >= 1.0 else 1.0

    # -------------------------
    # Combat logic
    # -------------------------

    def resolve_gem_combat(
        self,
        player,
        lock,
        player_gem_index: int,
        lock_gem_index: int
    ) -> None:
        """
        Resolves combat between a player's gem and a lock's gem.
        """

        # Chosen gems
        player_gem = player.get_gem(player_gem_index)
        lock_gem = lock.get_gem(lock_gem_index)

        # life of gems
        life_p = player_gem.life
        life_l = lock_gem.life

        # attack values of gems
        atk_p = player_gem.attack
        atk_l = lock_gem.attack

        # defense values of gems
        def_p = player_gem.defense
        def_l = lock_gem.defense

        # type values of gems
        type_p = player_gem.type
        type_l = lock_gem.type

        # Same type: both take damage
        if type_p == type_l:
            life_p -= (atk_l - def_p) * self._seconds
            life_l -= (atk_p - def_l) * self._seconds

            player.set_gem_life(player_gem_index, life_p)
            lock.set_gem_life(lock_gem_index, life_l)

        # Fire vs Metal
        elif type_p == "FUEGO" and type_l == "METAL":
            life_l -= (atk_p - def_l) * self._seconds
            lock.set_gem_life(lock_gem_index, life_l)

        elif type_p == "METAL" and type_l == "FUEGO":
            life_p -= (atk_l - def_p) * self._seconds
            player.set_gem_life(player_gem_index, life_p)

        # Water vs Metal
        elif type_p == "AGUA" and type_l == "METAL":
            life_p -= (atk_l - def_p) * self._seconds
            player.set_gem_life(player_gem_index, life_p)

        elif type_p == "METAL" and type_l == "AGUA":
            life_l -= (atk_p - def_l) * self._seconds
            lock.set_gem_life(lock_gem_index, life_l)

        # Fire vs Water
        elif type_p == "FUEGO" and type_l == "AGUA":
            life_p -= (atk_l - def_p) * self._seconds
            player.set_gem_life(player_gem_index, life_p)

        elif type_p == "AGUA" and type_l == "FUEGO":
            life_l -= (atk_p - def_l) * self._seconds
            lock.set_gem_life(lock_gem_index, life_l)

        else:
            print("Combat error occurred")