#!/usr/bin/env python3
"""
Reclassify verbs in 5_Common.md into 20 clear categories
"""

import re
from collections import defaultdict

# Define the 20 new categories and their keywords
CATEGORIES = {
    "MOVEMENT & TRAVEL": ["move", "go", "walk", "travel", "relocate", "transport", "arrive", "depart", "shift", "head", "cross", "navigate", "swing by", "drop by", "stop by", "come by", "enter", "exit", "rush", "dash", "scurry"],
    "BEGINNING & STARTING": ["start", "begin", "initiate", "kick off", "get the ball rolling", "commence", "launch", "restart", "ensue", "get things started", "set the wheels in motion"],
    "ENDING & COMPLETION": ["end", "finish", "complete", "terminate", "conclude", "stop", "cease", "wrap up", "wind up", "close"],
    "CHANGE & TRANSFORMATION": ["change", "transform", "modify", "alter", "convert", "transition", "evolve", "adapt", "adjust", "revise", "get better", "improve", "worsen", "assimilate", "modernize", "civilize", "privatize", "veer"],
    "COMMUNICATION": ["say", "tell", "speak", "talk", "communicate", "articulate", "express", "convey", "state", "declare", "announce", "mention", "discuss", "inform", "notify", "babble", "bulletin", "proclaim", "pronounce", "avow", "aver"],
    "COGNITIVE & THINKING": ["think", "consider", "ponder", "contemplate", "reflect", "understand", "comprehend", "realize", "recognize", "believe", "know", "remember", "forget", "brood", "deem", "delude", "deplore", "envisage", "misplace", "rue"],
    "AGREEMENT & PROMISE": ["agree", "disagree", "promise", "confirm", "verify", "guarantee", "assure", "ensure", "pledge", "vow", "consent", "approve", "reject", "refuse", "come around to", "buy into", "vouch for", "certify", "warrant", "validate"],
    "CONFLICT & AGGRESSION": ["fight", "attack", "defend", "challenge", "compete", "oppose", "resist", "confront", "battle", "struggle", "clash", "dispute", "argue"],
    "ACQUISITION & POSSESSION": ["get", "obtain", "acquire", "gain", "receive", "take", "grab", "seize", "capture", "catch", "fetch", "procure", "secure", "have", "possess", "own", "hold"],
    "GIVING & PROVIDING": ["give", "provide", "offer", "supply", "donate", "contribute", "present", "deliver", "grant", "bestow", "furnish", "animate", "decorate", "entitle", "exempt"],
    "CREATION & PRODUCTION": ["make", "create", "produce", "build", "construct", "manufacture", "generate", "form", "develop", "design", "craft", "fabricate"],
    "DESTRUCTION & DAMAGE": ["destroy", "damage", "break", "ruin", "demolish", "wreck", "shatter", "crush", "smash", "harm", "injure", "hurt", "impair", "disable", "sabotage"],
    "INCREASE & GROWTH": ["increase", "grow", "expand", "rise", "enlarge", "extend", "boost", "enhance", "augment", "amplify", "multiply", "swell", "escalate", "bulge", "germinate"],
    "DECREASE & REDUCTION": ["decrease", "reduce", "diminish", "shrink", "decline", "lessen", "lower", "cut", "minimize", "trim", "narrow", "contract", "dwindle"],
    "SHOWING & REVEALING": ["show", "display", "reveal", "demonstrate", "exhibit", "present", "indicate", "point out", "expose", "uncover", "disclose", "manifest", "describe"],
    "PHYSICAL CONTACT": ["touch", "hit", "strike", "grab", "hold", "grasp", "clutch", "grip", "pat", "rub", "stroke", "push", "pull", "press", "squeeze"],
    "CARE & SUPPORT": ["care", "support", "help", "assist", "aid", "protect", "guard", "look after", "look out for", "watch over", "tend", "nurture", "maintain", "sustain", "uphold"],
    "BEHAVIOR & ACTIONS": ["behave", "act", "hustle", "be on call", "be stuck with", "hold up", "put off", "set back", "be on standby", "remain on hand"],
    "CONTROL & INFLUENCE": ["control", "manage", "direct", "govern", "regulate", "influence", "affect", "impact", "sway", "manipulate", "dominate", "command", "rule", "oversee"],
    "TIME MANAGEMENT": ["delay", "hurry", "rush", "wait", "pause", "postpone", "drag on", "take ages", "take forever", "take a while"]
}

def read_file(filepath):
    """Read the entire file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.readlines()

def categorize_entry(entry_text):
    """Determine which category an entry belongs to based on keywords"""
    entry_lower = entry_text.lower()

    # Score each category
    scores = defaultdict(int)
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in entry_lower:
                scores[category] += 1

    # Return category with highest score, or None
    if scores:
        return max(scores.items(), key=lambda x: x[1])[0]
    return "OTHER"

def parse_file(lines):
    """Parse file and group entries by new categories"""
    categorized = defaultdict(list)
    current_section_lines = []

    for line in lines:
        # Skip file header
        if line.strip() == "# Common" or line.strip() == "":
            continue

        # Check if it's a section header
        if line.startswith("##"):
            continue

        # Check if it's a separator
        if line.strip() == "---":
            continue

        # Collect entry lines
        if line.strip():
            current_section_lines.append(line)

            # If this is a top-level entry (starts with - or >)
            if line.startswith(('- `', '> `')) and current_section_lines:
                # Categorize the collected lines
                entry_text = ''.join(current_section_lines)
                category = categorize_entry(entry_text)

                # Add to categorized dict
                if line.startswith('> `'):
                    categorized[category].append(entry_text)
                    current_section_lines = []
            # If it's a sub-entry, keep collecting
            elif line.startswith('  '):
                continue
            # If new top-level entry, save previous and start new
            elif current_section_lines and line.startswith('-'):
                if len(current_section_lines) > 1:
                    entry_text = ''.join(current_section_lines[:-1])
                    category = categorize_entry(entry_text)
                    categorized[category].append(entry_text)
                current_section_lines = [line]

    return categorized

def write_reclassified_file(categorized, output_path):
    """Write the reclassified content to a new file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Common\n\n")

        # Write each category
        for category in CATEGORIES.keys():
            if category in categorized and categorized[category]:
                f.write(f"## {category}\n")
                for entry in categorized[category]:
                    f.write(entry)
                    if not entry.endswith('\n'):
                        f.write('\n')
                f.write("\n")

        # Write OTHER category if any
        if "OTHER" in categorized and categorized["OTHER"]:
            f.write("## OTHER\n")
            for entry in categorized["OTHER"]:
                f.write(entry)
                if not entry.endswith('\n'):
                    f.write('\n')

if __name__ == "__main__":
    input_file = "/Users/tanamura/English/words/02_verb/5_Common.md"
    output_file = "/Users/tanamura/English/words/02_verb/5_Common_reclassified.md"

    print("Reading file...")
    lines = read_file(input_file)

    print("Parsing and categorizing entries...")
    categorized = parse_file(lines)

    print(f"Found {sum(len(v) for v in categorized.values())} entries")
    print(f"Categories: {list(categorized.keys())}")

    print("Writing reclassified file...")
    write_reclassified_file(categorized, output_file)

    print(f"Done! Output written to {output_file}")
