# Minecraft-Themed Data & Combat System

A personal project tracking my growth as a Python programmer, rebuilding the same idea across multiple versions.

## Version History

### V1
- First version, written using basic `if`/`elif` chains
- Simple inventory system (dict-based) with gathering, crafting, and smelting
- Flat achievement tracking

### V2
- Rewritten after learning about functions and data structures
- Switched from `if`/`elif` to `match`/`case`
- Achievements restructured from a flat dict to a list of dicts

### V3 — Complete
- Rebuilt from scratch to learn and apply Object-Oriented Programming
- Core class hierarchy: `Entity` → `Player` / `Mob` → `Skeleton`, each level adding or overriding only what's different
- Core OOP concepts demonstrated: classes & objects, `__init__`, methods & `self`, inheritance via `super()`, method overriding, and polymorphism
- `battle()` function handles a full sequence of fights against a list of mobs, using a `for` loop (per mob) nested with a `while` loop (per fight), with `return` used to cleanly exit both loops at once on player death
- Win, loss, and per-mob-defeat XP awarding all handled correctly
- Type hints added throughout

## Planned

### V3.5
- Weapon tiers affecting player damage
- Multiple mob types with distinct attack behavior (in progress: `Skeleton` done, more to come)

### V4
- Merge V2's inventory/crafting/smelting system with V3's OOP combat system into one unified game

## Goal

This project exists mainly to track my own progress — comparing how I structured code before and after learning new concepts (functions, then OOP).
