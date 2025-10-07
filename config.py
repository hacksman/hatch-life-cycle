"""Configuration settings for the step counter pet app."""
from __future__ import annotations

from enum import Enum
from typing import ClassVar


class ItemTier(Enum):
    """Available item tiers."""

    BASIC = "basic"
    PREMIUM = "premium"


class ItemCategory(Enum):
    """Available item categories in the store."""

    FOOD = "food"
    MEDICINE = "medicine"
    BATH = "bath"


class StepCounter:
    """Step counter configuration."""

    default_goal: ClassVar[int] = 10_000
    minimum_goal: ClassVar[int] = 1_000
    maximum_goal: ClassVar[int] = 20_000


class Pet:
    """Pet configuration settings."""

    class Experience:
        base_exp: ClassVar[int] = 100
        multiplier: ClassVar[float] = 1.2

        feeding: ClassVar[int] = 5
        bathing: ClassVar[int] = 3
        healing: ClassVar[int] = 4

    class StatusThreshold:
        dying: ClassVar[int] = 0
        sad: ClassVar[int] = 25
        unhappy: ClassVar[int] = 75
        full: ClassVar[int] = 100

    class Stage:
        baby_level_range: ClassVar[range] = range(1, 4)
        adult_level_range: ClassVar[range] = range(4, 8)
        mature_level_range: ClassVar[range] = range(8, 12)

        baby_height: ClassVar[int] = 10
        adult_height: ClassVar[int] = 12
        mature_height: ClassVar[int] = 14

    class InitialStatus:
        health: ClassVar[int] = 75
        hunger: ClassVar[int] = 50
        cleanliness: ClassVar[int] = 60

    class StatusValues:
        max_value: ClassVar[int] = 100

        class MaxStatus:
            health: ClassVar[int] = 100
            hunger: ClassVar[int] = 100
            cleanliness: ClassVar[int] = 100
            happiness: ClassVar[int] = 100

    class LevelEnergy:
        class Basic:
            energy: ClassVar[int] = 10

        class Premium:
            energy: ClassVar[int] = 20

        @staticmethod
        def energy(tier: ItemTier) -> int:
            if tier is ItemTier.BASIC:
                return Pet.LevelEnergy.Basic.energy
            if tier is ItemTier.PREMIUM:
                return Pet.LevelEnergy.Premium.energy
            raise ValueError(f"Unsupported item tier: {tier}")

    class StorePrice:
        class Food:
            basic: ClassVar[int] = 20
            premium: ClassVar[int] = 40

        class Medicine:
            basic: ClassVar[int] = 25
            premium: ClassVar[int] = 45

        class Bath:
            basic: ClassVar[int] = 15
            premium: ClassVar[int] = 30

        @staticmethod
        def price(category: ItemCategory, tier: ItemTier) -> int:
            match category:
                case ItemCategory.FOOD:
                    return (
                        Pet.StorePrice.Food.basic
                        if tier is ItemTier.BASIC
                        else Pet.StorePrice.Food.premium
                    )
                case ItemCategory.MEDICINE:
                    return (
                        Pet.StorePrice.Medicine.basic
                        if tier is ItemTier.BASIC
                        else Pet.StorePrice.Medicine.premium
                    )
                case ItemCategory.BATH:
                    return (
                        Pet.StorePrice.Bath.basic
                        if tier is ItemTier.BASIC
                        else Pet.StorePrice.Bath.premium
                    )
            raise ValueError(f"Unsupported item category: {category}")


class StatusDecay:
    interval: ClassVar[int] = 300
    hunger_rate: ClassVar[int] = 4
    cleanliness_rate: ClassVar[int] = 3
    health_rate: ClassVar[int] = 2


class Runaway:
    check_threshold: ClassVar[int] = 50
    base_probability: ClassVar[float] = 0.03
    extra_probability_per_low_stat: ClassVar[float] = 0.04
    probability_cap: ClassVar[float] = 0.8
    min_return_hours: ClassVar[int] = 2
    max_return_hours: ClassVar[int] = 6


class Exchange:
    steps_to_coins_rate: ClassVar[int] = 10
    rate_display_text: ClassVar[str] = f"{steps_to_coins_rate} Steps = 1 Coin"
    exchangeable_days: ClassVar[int] = 7


class InitialResources:
    coins: ClassVar[int] = 250

    class Inventory:
        bread: ClassVar[int] = 15
        rice: ClassVar[int] = 18
        cookie: ClassVar[int] = 10
        chicken: ClassVar[int] = 13
        candy: ClassVar[int] = 22

        medicinebox: ClassVar[int] = 13
        inject_shot: ClassVar[int] = 14
        capsule: ClassVar[int] = 14

        shower: ClassVar[int] = 16
        bubble_bath: ClassVar[int] = 14


class NaturalGrowth:
    class DaysExperience:
        per_day: ClassVar[int] = 10

    class FeedingExperience:
        per_feeding: ClassVar[int] = 5
