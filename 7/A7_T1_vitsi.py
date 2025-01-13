from typing import TypeAlias                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;ಠ益ಠ = "Insert positive integer(negative stops): ";ʘ‿ʘ = "Stopped collecting positive integers.";ϞϞ_ϞϞ = "No integers to display.";ΩツΩ = "Displaying";ポ_ポ = "integers:";ミ_ミ = "Program starting.";Ц_Ц = "Collect positive integers.";π_π = "Program ending.";Θ_Θ: TypeAlias = None;Ω_ツ = None;益_益 = list;シ_シ = int;リ_リ = enumerate;ヮ_ヮ = print;ョ_ョ = 益_益.append;ΛΩΛ = 益_益.clear;ナ_ナ = len;ω_Ω = input;ᓂ = 0;リ = 1;ж = "- Index ";Λ = "=> Ordinal";ミ = "=> Integer";  # noqa


def ಠ_ಠ(ಠ‿ಠ: 益_益[シ_シ]) -> Θ_Θ:
    while (ツ_Λ := シ_シ(ω_Ω(ಠ益ಠ))) >= ᓂ:
        ョ_ョ(ಠ‿ಠ, ツ_Λ)
    ヮ_ヮ(ʘ‿ʘ)
    return Ω_ツ


def ᓚᘏᗢ(ಠ‿ಠ: 益_益[シ_シ]) -> Θ_Θ:
    if ナ_ナ(ಠ‿ಠ) == ᓂ:
        ヮ_ヮ(ϞϞ_ϞϞ)
        return Ω_ツ
    ヮ_ヮ(f"{ΩツΩ} {ナ_ナ(ಠ‿ಠ)} {ポ_ポ}")
    for ツ, シ in リ_リ(ಠ‿ಠ):
        ヮ_ヮ(f"{ж} {ツ} {Λ} {ツ + リ} {ミ} {シ}")
    return Ω_ツ


def ᓀ_ᓂ() -> Θ_Θ:
    ヮ_ヮ(ミ_ミ)
    ヮ_ヮ(Ц_Ц)
    ಠ‿ಠ: 益_益[シ_シ] = 益_益()
    ಠ_ಠ(ಠ‿ಠ)
    ᓚᘏᗢ(ಠ‿ಠ)
    ヮ_ヮ(π_π)
    return Ω_ツ


ᓀ_ᓂ()
