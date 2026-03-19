#!/usr/bin/env python3
"""
Replacement engine for the UI design system configuration.
Reads config JSON from stdin, modifies all skill files accordingly.
"""

import sys
import os
import json
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(SCRIPT_DIR)

# Tailwind color hex palette (shade -> hex)
TAILWIND_COLORS = {
    "slate": {50:"#F8FAFC",100:"#F1F5F9",200:"#E2E8F0",300:"#CBD5E1",400:"#94A3B8",500:"#64748B",600:"#475569",700:"#334155",800:"#1E293B",900:"#0F172A",950:"#020617"},
    "gray": {50:"#F9FAFB",100:"#F3F4F6",200:"#E5E7EB",300:"#D1D5DB",400:"#9CA3AF",500:"#6B7280",600:"#4B5563",700:"#374151",800:"#1F2937",900:"#111827",950:"#030712"},
    "zinc": {50:"#FAFAFA",100:"#F4F4F5",200:"#E4E4E7",300:"#D4D4D8",400:"#A1A1AA",500:"#71717A",600:"#52525B",700:"#3F3F46",800:"#27272A",900:"#18181B",950:"#09090B"},
    "neutral": {50:"#FAFAFA",100:"#F5F5F5",200:"#E5E5E5",300:"#D4D4D4",400:"#A3A3A3",500:"#737373",600:"#525252",700:"#404040",800:"#262626",900:"#171717",950:"#0A0A0A"},
    "stone": {50:"#FAFAF9",100:"#F5F5F4",200:"#E7E5E3",300:"#D6D3D1",400:"#A8A29E",500:"#78716C",600:"#57534E",700:"#44403C",800:"#292524",900:"#1C1917",950:"#0C0A09"},
    "red": {50:"#FEF2F2",100:"#FEE2E2",200:"#FECACA",300:"#FCA5A5",400:"#F87171",500:"#EF4444",600:"#DC2626",700:"#B91C1C",800:"#991B1B",900:"#7F1D1D",950:"#450A0A"},
    "orange": {50:"#FFF7ED",100:"#FFEDD5",200:"#FED7AA",300:"#FDBA74",400:"#FB923C",500:"#F97316",600:"#EA580C",700:"#C2410C",800:"#9A3412",900:"#7C2D12",950:"#431407"},
    "amber": {50:"#FFFBEB",100:"#FEF3C7",200:"#FDE68A",300:"#FCD34D",400:"#FBBF24",500:"#F59E0B",600:"#D97706",700:"#B45309",800:"#92400E",900:"#78350F",950:"#451A03"},
    "yellow": {50:"#FEFCE8",100:"#FEF9C3",200:"#FEF08A",300:"#FDE047",400:"#FACC15",500:"#EAB308",600:"#CA8A04",700:"#A16207",800:"#854D0E",900:"#713F12",950:"#422006"},
    "lime": {50:"#F7FEE7",100:"#ECFCCB",200:"#D9F99D",300:"#BEF264",400:"#A3E635",500:"#84CC16",600:"#65A30D",700:"#4D7C0F",800:"#3F6212",900:"#365314",950:"#1A2E05"},
    "green": {50:"#F0FDF4",100:"#DCFCE7",200:"#BBF7D0",300:"#86EFAC",400:"#4ADE80",500:"#22C55E",600:"#16A34A",700:"#15803D",800:"#166534",900:"#14532D",950:"#052E16"},
    "emerald": {50:"#ECFDF5",100:"#D1FAE5",200:"#A7F3D0",300:"#6EE7B7",400:"#34D399",500:"#10B981",600:"#059669",700:"#047857",800:"#065F46",900:"#064E3B",950:"#022C22"},
    "teal": {50:"#F0FDFA",100:"#CCFBF1",200:"#99F6E4",300:"#5EEAD4",400:"#2DD4BF",500:"#14B8A6",600:"#0D9488",700:"#0F766E",800:"#115E59",900:"#134E4A",950:"#042F2E"},
    "cyan": {50:"#ECFEFF",100:"#CFFAFE",200:"#A5F3FC",300:"#67E8F9",400:"#22D3EE",500:"#06B6D4",600:"#0891B2",700:"#0E7490",800:"#155E75",900:"#164E63",950:"#083344"},
    "sky": {50:"#F0F9FF",100:"#E0F2FE",200:"#BAE6FD",300:"#7DD3FC",400:"#38BDF8",500:"#0EA5E9",600:"#0284C7",700:"#0369A1",800:"#075985",900:"#0C4A6E",950:"#082F49"},
    "blue": {50:"#EFF6FF",100:"#DBEAFE",200:"#BFDBFE",300:"#93C5FD",400:"#60A5FA",500:"#3B82F6",600:"#2563EB",700:"#1D4ED8",800:"#1E40AF",900:"#1E3A8A",950:"#172554"},
    "indigo": {50:"#EEF2FF",100:"#E0E7FF",200:"#C7D2FE",300:"#A5B4FC",400:"#818CF8",500:"#6366F1",600:"#4F46E5",700:"#4338CA",800:"#3730A3",900:"#312E81",950:"#1E1B4B"},
    "violet": {50:"#F5F3FF",100:"#EDE9FE",200:"#DDD6FE",300:"#C4B5FD",400:"#A78BFA",500:"#8B5CF6",600:"#7C3AED",700:"#6D28D9",800:"#5B21B6",900:"#4C1D95",950:"#2E1065"},
    "purple": {50:"#FAF5FF",100:"#F3E8FF",200:"#E9D5FF",300:"#D8B4FE",400:"#C084FC",500:"#A855F7",600:"#9333EA",700:"#7E22CE",800:"#6B21A8",900:"#581C87",950:"#3B0764"},
    "fuchsia": {50:"#FDF4FF",100:"#FAE8FF",200:"#F5D0FE",300:"#F0ABFC",400:"#E879F9",500:"#D946EF",600:"#C026D3",700:"#A21CAF",800:"#86198F",900:"#701A75",950:"#4A044E"},
    "pink": {50:"#FDF2F8",100:"#FCE7F3",200:"#FBCFE8",300:"#F9A8D4",400:"#F472B6",500:"#EC4899",600:"#DB2777",700:"#BE185D",800:"#9D174D",900:"#831843",950:"#500724"},
    "rose": {50:"#FFF1F2",100:"#FFE4E6",200:"#FECDD3",300:"#FDA4AF",400:"#FB7185",500:"#F43F5E",600:"#E11D48",700:"#BE123C",800:"#9F1239",900:"#881337",950:"#4C0519"},
}

# Default configuration
DEFAULTS = {
    "primary": "indigo",
    "accent": "amber",
    "neutral": "gray",
    "success": "emerald",
    "warning": "amber",
    "error": "rose",
    "info": "blue",
    "font_display": "Plus Jakarta Sans",
    "font_mono": "JetBrains Mono",
    "radius": "rounded-lg",
    "radius_sm": "rounded-md",
}

# Files to modify (relative to SKILL_DIR)
TARGET_FILES = [
    "SKILL.md",
    "colors.md",
    "typography.md",
    "patterns.md",
    "animations.md",
    "overlays.md",
    "scripts/setup-design-system.sh",
    "scripts/setup-fonts.sh",
]

# Section markers for protected regions (content that should NOT be modified)
# These mark the start/end of the "Alternative Primary Fonts" section in typography.md
ALT_FONTS_START = "### Alternative Primary Fonts"
ALT_FONTS_END = "### Monospace Font"

# Radius mapping: chosen radius -> input radius (one step smaller)
RADIUS_MAP = {
    "rounded-none": "rounded-none",
    "rounded-sm": "rounded-sm",
    "rounded-md": "rounded-sm",
    "rounded-lg": "rounded-md",
    "rounded-xl": "rounded-lg",
    "rounded-2xl": "rounded-xl",
    "rounded-full": "rounded-xl",
}

# Font name utilities
def font_import_name(display_name):
    """Plus Jakarta Sans -> Plus_Jakarta_Sans"""
    return display_name.replace(" ", "_")

def font_camel_name(display_name):
    """Plus Jakarta Sans -> plusJakartaSans"""
    parts = display_name.split()
    if not parts:
        return ""
    result = parts[0].lower()
    for p in parts[1:]:
        result += p.capitalize()
    return result

def get_hex(color_name, shade):
    """Get hex code for a Tailwind color + shade."""
    if color_name in TAILWIND_COLORS and shade in TAILWIND_COLORS[color_name]:
        return TAILWIND_COLORS[color_name][shade]
    return None

def get_primary_hex(color_name):
    """Get the '600' shade hex as the primary representative hex."""
    return get_hex(color_name, 600)

def get_accent_hex(color_name):
    """Get the '500' shade hex as the accent representative hex."""
    return get_hex(color_name, 500)


def replace_color_classes(text, old_color, new_color):
    """Replace all Tailwind color class references: old-50 -> new-50, etc."""
    if old_color == new_color:
        return text
    # Match color-shade patterns (e.g., indigo-600, gray-50, etc.)
    pattern = re.compile(r'\b' + re.escape(old_color) + r'-(\d{2,3})\b')
    return pattern.sub(new_color + r'-\1', text)


def replace_hex_in_headings(text, old_color, new_color, shade):
    """Replace hex codes that appear in markdown headings for a given color."""
    old_hex = get_hex(old_color, shade)
    new_hex = get_hex(new_color, shade)
    if old_hex and new_hex and old_hex != new_hex:
        text = text.replace(old_hex, new_hex)
    return text


def replace_font(text, old_display, new_display):
    """Replace all three forms of a font name using context-aware replacement."""
    if old_display == new_display:
        return text
    old_import = font_import_name(old_display)
    new_import = font_import_name(new_display)
    old_camel = font_camel_name(old_display)
    new_camel = font_camel_name(new_display)

    # If old font has multi-word name, all three forms are distinct - use placeholders
    if old_import != old_display:
        # Replace longest first to avoid partial matches
        text = text.replace(old_import, "<<FONT_IMPORT>>")
        text = text.replace(old_camel, "<<FONT_CAMEL>>")
        text = text.replace(old_display, "<<FONT_DISPLAY>>")
        text = text.replace("<<FONT_IMPORT>>", new_import)
        text = text.replace("<<FONT_CAMEL>>", new_camel)
        text = text.replace("<<FONT_DISPLAY>>", new_display)
    else:
        # Single-word font (e.g. "Inter") - all forms are the same.
        # Use context-aware line-by-line replacement.
        lines = text.split('\n')
        result = []
        for line in lines:
            if old_display not in line and old_camel not in line:
                result.append(line)
                continue
            # camelCase form (e.g. "inter" as variable name)
            if old_camel != old_display:
                line = line.replace(old_camel, new_camel)
            # Import context: "import { Inter }" or "const inter = Inter({"
            # Use regex to match code import patterns
            line = re.sub(
                r'import\s*\{\s*' + re.escape(old_display) + r'\s*\}',
                f'import {{ {new_import} }}',
                line
            )
            # Variable assignment: "= Inter({" -> "= New_Font({"
            line = re.sub(
                r'=\s*' + re.escape(old_display) + r'\(',
                f'= {new_import}(',
                line
            )
            # grep -q "Inter" -> grep -q "New_Font"
            line = re.sub(
                r'grep\s+-q\s+"' + re.escape(old_display) + r'"',
                f'grep -q "{new_import}"',
                line
            )
            # Font name in prose, Tailwind config, etc - display form
            # But avoid re-replacing the import we just fixed
            if new_import in line:
                # Already handled import context, replace remaining display occurrences
                # Split on the import name to protect it
                parts = line.split(new_import)
                parts = [p.replace(old_display, new_display) for p in parts]
                line = new_import.join(parts)
            else:
                line = line.replace(old_display, new_display)
            result.append(line)
        text = '\n'.join(result)
    return text


def replace_radius(text, old_radius, new_radius, old_radius_sm, new_radius_sm):
    """Replace radius classes in className strings using a placeholder to avoid cascading."""
    if old_radius == new_radius and old_radius_sm == new_radius_sm:
        return text
    # Use placeholders to prevent cascading replacements
    placeholder_main = "<<RADIUS_MAIN>>"
    placeholder_sm = "<<RADIUS_SM>>"
    if old_radius != new_radius:
        text = text.replace(old_radius, placeholder_main)
    if old_radius_sm != new_radius_sm:
        text = text.replace(old_radius_sm, placeholder_sm)
    text = text.replace(placeholder_main, new_radius)
    text = text.replace(placeholder_sm, new_radius_sm)
    return text


def process_amber_dual_role(text, config, old_config):
    """
    Handle amber's dual role as both accent and warning color.

    In the original files, 'amber' is used for BOTH accent and warning.
    We need to distinguish between them based on context:
    - Accent context: ### Accent headings, button.ghost, highlight badges
    - Warning context: ### Warning headings, status.warning, Warning: labels
    """
    old_accent = old_config.get("accent", "amber")
    old_warning = old_config.get("warning", "amber")
    new_accent = config.get("accent", "amber")
    new_warning = config.get("warning", "amber")

    # If old accent and warning were different, simple replacement works
    if old_accent != old_warning:
        text = replace_color_classes(text, old_accent, new_accent)
        text = replace_color_classes(text, old_warning, new_warning)
        return text

    # Both were the same (e.g., both "amber") - need section-aware replacement
    shared_color = old_accent  # e.g., "amber"

    if new_accent == new_warning:
        # Both going to same color - simple replace
        text = replace_color_classes(text, shared_color, new_accent)
        return text

    if shared_color == new_accent:
        # Only warning changed - process warning sections
        text = _replace_in_sections(text, shared_color, new_warning, "warning")
        return text

    if shared_color == new_warning:
        # Only accent changed - process accent sections
        text = _replace_in_sections(text, shared_color, new_accent, "accent")
        return text

    # Both changed to different colors - need to split
    # First, replace warning contexts, then accent contexts
    # We do warning first (more specific sections), then accent gets the rest

    # Strategy: replace ALL with accent first, then fix warning sections
    text = replace_color_classes(text, shared_color, new_accent)
    # Now replace accent->warning in warning-specific sections
    text = _replace_in_sections(text, new_accent, new_warning, "warning")

    return text


def _replace_in_sections(text, old_color, new_color, section_type):
    """Replace color within specific section contexts."""
    lines = text.split('\n')
    result = []
    in_target_section = False

    for line in lines:
        # Detect section headings
        stripped = line.strip()

        if section_type == "warning":
            # Warning sections
            if re.match(r'^###\s+Warning', stripped, re.IGNORECASE):
                in_target_section = True
            elif stripped.startswith('### ') and re.match(r'^###\s+(Accent|Success|Error|Info|Destructive|Primary|Neutrals|Secondary|Premium)', stripped):
                in_target_section = False
            elif re.match(r'^##\s+', stripped) and not stripped.startswith('### '):
                in_target_section = False

            # Also handle inline status lines like "Warning:  bg-amber-50..."
            if re.match(r'^Warning:', stripped):
                in_target_section = True
                line = replace_color_classes(line, old_color, new_color)
                result.append(line)
                in_target_section = False
                continue

            # Handle status.warning in implementation object
            if "warning:" in stripped.lower() and old_color + "-" in stripped:
                line = replace_color_classes(line, old_color, new_color)
                result.append(line)
                continue

            # Handle dark mode warning lines
            if in_target_section:
                line = replace_color_classes(line, old_color, new_color)

            # Handle compact status blocks (Warning: on same line with label)
            if 'Warning:' in line and old_color + '-' in line:
                line = replace_color_classes(line, old_color, new_color)

        elif section_type == "accent":
            # Accent sections - detect ## or ### Accent heading, stay active until next ## heading
            if re.match(r'^#{2,3}\s+Accent', stripped, re.IGNORECASE):
                in_target_section = True
            elif re.match(r'^##\s+', stripped) and not re.match(r'^##\s+Accent', stripped, re.IGNORECASE) and not stripped.startswith('### '):
                in_target_section = False
            # A ### heading that is NOT "Usage" or similar sub-heading of the accent section
            # and IS a known other section like "Warning", "Success", etc. should end the section
            elif stripped.startswith('### ') and re.match(r'^###\s+(Warning|Success|Error|Info|Destructive|Semantic|Primary|Neutrals|Secondary)', stripped):
                in_target_section = False

            # Handle ghost button and accent in implementation object
            if "ghost:" in stripped.lower() and old_color + "-" in stripped:
                line = replace_color_classes(line, old_color, new_color)
                result.append(line)
                continue

            if in_target_section:
                line = replace_color_classes(line, old_color, new_color)

            # Handle "Highlight" / "Featured" / "Accent" labeled badges
            if ('Highlight' in line or 'Featured' in line or 'Accent' in line or 'Popular' in line) and old_color + '-' in line:
                line = replace_color_classes(line, old_color, new_color)

        result.append(line)

    return '\n'.join(result)


def update_heading_hex(text, old_color, new_color, shade, heading_pattern):
    """Update hex codes in specific heading lines."""
    old_hex = get_hex(old_color, shade)
    new_hex = get_hex(new_color, shade)
    if not old_hex or not new_hex or old_hex == new_hex:
        return text

    lines = text.split('\n')
    result = []
    for line in lines:
        if re.match(heading_pattern, line.strip()):
            line = line.replace(old_hex, new_hex)
        result.append(line)
    return '\n'.join(result)


def update_color_heading_name(text, old_color, new_color):
    """Update color name in markdown headings like '### Primary: Indigo (#4F46E5)'."""
    old_title = old_color.capitalize()
    new_title = new_color.capitalize()
    old_hex = get_hex(old_color, 600) or ""
    new_hex = get_hex(new_color, 600) or ""

    if old_hex and new_hex:
        text = text.replace(f": {old_title} ({old_hex})", f": {new_title} ({new_hex})")
    text = text.replace(f": {old_title} (", f": {new_title} (")
    return text


def process_file(filepath, config, old_config):
    """Process a single file with all replacements."""
    with open(filepath, 'r') as f:
        text = f.read()

    original = text

    old_primary = old_config.get("primary", "indigo")
    old_neutral = old_config.get("neutral", "gray")
    old_success = old_config.get("success", "emerald")
    old_error = old_config.get("error", "rose")
    old_info = old_config.get("info", "blue")
    old_font_display = old_config.get("font_display", "Plus Jakarta Sans")
    old_font_mono = old_config.get("font_mono", "JetBrains Mono")
    old_radius = old_config.get("radius", "rounded-lg")
    old_radius_sm = old_config.get("radius_sm", "rounded-md")

    new_primary = config.get("primary", "indigo")
    new_accent = config.get("accent", "amber")
    new_neutral = config.get("neutral", "gray")
    new_success = config.get("success", "emerald")
    new_warning = config.get("warning", "amber")
    new_error = config.get("error", "rose")
    new_info = config.get("info", "blue")
    new_font_display = config.get("font_display", "Plus Jakarta Sans")
    new_font_mono = config.get("font_mono", "JetBrains Mono")
    new_radius = config.get("radius", "rounded-lg")
    new_radius_sm = config.get("radius_sm", RADIUS_MAP.get(new_radius, "rounded-md"))

    # 1. Replace primary color (simple global replace)
    text = replace_color_classes(text, old_primary, new_primary)

    # 2. Replace neutral color
    text = replace_color_classes(text, old_neutral, new_neutral)

    # 3. Replace success color
    text = replace_color_classes(text, old_success, new_success)

    # 4. Replace error color
    text = replace_color_classes(text, old_error, new_error)

    # 5. Replace info color
    text = replace_color_classes(text, old_info, new_info)

    # 6. Handle amber dual-role (accent + warning)
    text = process_amber_dual_role(text, config, old_config)

    # 7. Update heading names BEFORE hex replacement (so hex patterns still match)
    text = update_color_heading_name(text, old_primary, new_primary)

    # Update accent heading names (handles both "Accent: Amber" and "Accent Color: Amber")
    old_accent_color = old_config.get("accent", "amber")
    old_accent_title = old_accent_color.capitalize()
    new_accent_title = new_accent.capitalize()
    accent_old_hex = get_hex(old_accent_color, 500) or ""
    accent_new_hex = get_hex(new_accent, 500) or ""
    # Replace with hex
    if accent_old_hex and accent_new_hex:
        text = text.replace(
            f"Accent Color: {old_accent_title} ({accent_old_hex})",
            f"Accent Color: {new_accent_title} ({accent_new_hex})"
        )
        text = text.replace(
            f"Accent: {old_accent_title} ({accent_old_hex})",
            f"Accent: {new_accent_title} ({accent_new_hex})"
        )
    # Fallback patterns without specific hex match
    text = text.replace(f"Accent Color: {old_accent_title} (", f"Accent Color: {new_accent_title} (")
    text = text.replace(f"Accent: {old_accent_title} (", f"Accent: {new_accent_title} (")

    # Update hex values in headings and color scale listings
    for shade in [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]:
        text = replace_hex_in_headings(text, old_primary, new_primary, shade)
        text = replace_hex_in_headings(text, old_neutral, new_neutral, shade)
        text = replace_hex_in_headings(text, old_success, new_success, shade)
        text = replace_hex_in_headings(text, old_error, new_error, shade)
        text = replace_hex_in_headings(text, old_info, new_info, shade)
        # Accent hex codes
        text = replace_hex_in_headings(text, old_accent_color, new_accent, shade)

    # 8. Replace fonts (protecting the "Alternative Primary Fonts" section)
    # Extract and protect the alternatives section if present
    alt_section = None
    if ALT_FONTS_START in text and ALT_FONTS_END in text:
        start_idx = text.index(ALT_FONTS_START)
        end_idx = text.index(ALT_FONTS_END)
        alt_section = text[start_idx:end_idx]
        text = text[:start_idx] + "<<ALT_FONTS_PROTECTED>>" + text[end_idx:]

    text = replace_font(text, old_font_display, new_font_display)
    text = replace_font(text, old_font_mono, new_font_mono)

    # Restore protected section
    if alt_section is not None:
        text = text.replace("<<ALT_FONTS_PROTECTED>>", alt_section)

    # 9. Replace radius
    text = replace_radius(text, old_radius, new_radius, old_radius_sm, new_radius_sm)

    if text != original:
        with open(filepath, 'w') as f:
            f.write(text)
        return True
    return False


def main():
    config_input = sys.stdin.buffer.read()
    config = json.loads(config_input)

    # Load previous config for understanding what to replace FROM
    config_path = os.path.join(SCRIPT_DIR, "config.json")
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            old_config = json.load(f)
    else:
        old_config = dict(DEFAULTS)

    # Compute radius_sm from radius if not set
    if "radius_sm" not in config:
        config["radius_sm"] = RADIUS_MAP.get(config.get("radius", "rounded-lg"), "rounded-md")
    if "radius_sm" not in old_config:
        old_config["radius_sm"] = RADIUS_MAP.get(old_config.get("radius", "rounded-lg"), "rounded-md")

    modified = []
    for rel_path in TARGET_FILES:
        filepath = os.path.join(SKILL_DIR, rel_path)
        if os.path.exists(filepath):
            if process_file(filepath, config, old_config):
                modified.append(rel_path)

    # Save config
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)

    if modified:
        print(f"Modified {len(modified)} files: {', '.join(modified)}")
    else:
        print("No changes needed.")


if __name__ == "__main__":
    main()
