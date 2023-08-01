import math
from typing import Literal

from skykings_weight.data import dungeon_groups, skill_groups, slayer_groups

__all__ = (
    "dungeon_weight",
    "slayer_weight",
    "skill_weight",
)


def dungeon_weight(
    category: Literal["catacombs", "healer", "mage", "berserk", "archer", "tank"],
    level: float,
    xp: float | int
) -> tuple[float, float]:
    """
    Calculates the weight of a dungeon class or the catacombs skill.
    :param category: ``catacombs`` for catacombs skill, ``healer``,
        ``mage``, ``berserk``, ``archer``, ``tank`` for dungeon classes.
    :type category: Literal["catacombs", "healer", "mage", "berserk", "archer", "tank"]
    :param level: The skill or class' level, including partial progress.
    :type level: float
    :param xp: The skill or class' total experience.
    :type xp: float | int
    :return: A tuple containing the calculated weight and overflow.
    :rtype: tuple[float, float]
    """
    percentageModifier = dungeon_groups[category]
    base = (level ** 4.5) * percentageModifier
    if xp <= 569809640:
        return base, 0
    remaining = xp - 569809640
    splitter = (4 * 569809640) / base
    return math.floor(base), remaining / splitter ** 0.968


def slayer_weight(
    slayer: Literal["zombie", "spider", "wolf", "enderman", "blaze", "vampire"],
    xp: float | int
) -> tuple[float, float]:
    """
    Calculates the weight of a slayer.
    :param slayer: The slayer to calculate.
    :type slayer: Literal["zombie", "spider", "wolf", "enderman", "blaze", "vampire"]
    :param xp: The slayer's experience.
    :type xp: float | int
    :return: A tuple containing the calculated weight and overflow.
    :rtype: tuple[float, float]
    """
    slayerGroup = slayer_groups[slayer]
    xp_cap = (2400 if slayer == "vampire" else 1000000)
    if xp <= xp_cap:
        if xp == 0:
            weight = 0
        else:
            weight = xp / slayerGroup["divider"]
        return weight, 0
    count_over_max = (xp - xp_cap) / xp_cap
    base = xp_cap / slayerGroup["divider"]
    return base, count_over_max * base * slayerGroup["modifier"]


def skill_weight(
    skill: Literal[
        "alchemy", "carpentry", "combat", "enchanting", "farming", "fishing", "foraging", "mining", "taming"
    ],
    level: float,
    xp: float | int,
) -> tuple[float, float]:
    """
    Calculates the weight of a skill.
    :param skill: The skill to calculate.
    :type skill: Literal[
        "alchemy", "carpentry", "combat", "enchanting", "farming", "fishing", "foraging", "mining", "taming"
        ]
    :param level: The skill's level, including partial progress.
    :type level: float
    :param xp: The skill's experience.
    :type xp: float | int
    :return: A tuple containing the calculated weight and overflow.
    :rtype: tuple[float, float]
    """
    skillGroup = skill_groups[skill]
    if skillGroup["maxLevel"] == 50:
        maxSkillLevelXP = 55172425
    else:
        maxSkillLevelXP = 111672425
    base = ((level * 10) ** (0.5 + skillGroup["exponent"] + level / 100)) / 1250
    if xp > maxSkillLevelXP:
        base = round(base)
    else:
        return base, 0
    return base, (xp - maxSkillLevelXP) / skillGroup["divider"] ** 0.968
