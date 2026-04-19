# features/tips.py

from features.stats import get_worst_subject

# --- Subject-to-resources mapping ---
RESOURCES = {
    "math": [
        "Khan Academy (Math): https://www.khanacademy.org/math",
        "Paul's Online Math Notes: https://tutorial.math.lamar.edu",
        "Wolfram Alpha: https://www.wolframalpha.com",
    ],
    "english": [
        "Purdue OWL (Writing): https://owl.purdue.edu",
        "Grammarly Blog: https://www.grammarly.com/blog",
        "SparkNotes: https://www.sparknotes.com",
    ],
    "science": [
        "Khan Academy (Science): https://www.khanacademy.org/science",
        "CK-12: https://www.ck12.org",
        "PhET Interactive Simulations: https://phet.colorado.edu",
    ],
    "history": [
        "Khan Academy (History): https://www.khanacademy.org/humanities/world-history",
        "Crash Course History (YouTube): https://www.youtube.com/user/crashcourse",
        "JSTOR (Articles): https://www.jstor.org",
    ],
    "programming": [
        "freeCodeCamp: https://www.freecodecamp.org",
        "The Odin Project: https://www.theodinproject.com",
        "LeetCode (Practice): https://leetcode.com",
    ],
    "biology": [
        "Khan Academy (Biology): https://www.khanacademy.org/science/biology",
        "Biology Online: https://www.biology-online.org",
        "Visible Body: https://www.visiblebody.com",
    ],
    "chemistry": [
        "Khan Academy (Chemistry): https://www.khanacademy.org/science/chemistry",
        "ChemLibreTexts: https://chem.libretexts.org",
        "Royal Society of Chemistry: https://www.rsc.org/learn-chemistry",
    ],
    "default": [
        "Khan Academy: https://www.khanacademy.org",
        "Coursera: https://www.coursera.org",
        "YouTube (search your subject): https://www.youtube.com",
    ],
}

# --- Subject-to-tips mapping ---
TIPS = {
    "math": [
        "Practice problems daily — even just 10 minutes helps build fluency.",
        "Work through mistakes: understand *why* an answer was wrong.",
        "Draw diagrams for word problems to visualize what's being asked.",
    ],
    "english": [
        "Read a little every day to build vocabulary and comprehension.",
        "Write a short journal entry to practice putting thoughts into words.",
        "Outline essays before writing to organize your argument clearly.",
    ],
    "science": [
        "Connect concepts to real-world examples to make them stick.",
        "Use flashcards for definitions and formulas.",
        "Watch experiment videos to reinforce lab concepts visually.",
    ],
    "history": [
        "Create timelines to understand cause-and-effect relationships.",
        "Focus on themes (war, economy, culture) rather than memorizing dates.",
        "Summarize events in your own words after reading.",
    ],
    "programming": [
        "Code every day — even small practice problems count.",
        "Read other people's code on GitHub to pick up new patterns.",
        "Break problems into smaller pieces before writing any code.",
    ],
    "biology": [
        "Use diagrams and labeled drawings to learn structures.",
        "Group related concepts (e.g., all cell organelles) for easier recall.",
        "Teach the material to a friend or out loud to yourself.",
    ],
    "chemistry": [
        "Memorize the periodic table in sections, not all at once.",
        "Balance equations step-by-step and check your atom counts.",
        "Use mnemonics for reaction types and element groups.",
    ],
    "default": [
        "Break study sessions into 25-minute focused blocks (Pomodoro technique).",
        "Review notes within 24 hours of a session to boost retention.",
        "Get enough sleep — memory consolidation happens during rest.",
    ],
}


def _normalize(subject):
    return subject.strip().lower()


def get_tips(subject):
    """Return a list of study tips for the given subject."""
    key = _normalize(subject)
    return TIPS.get(key, TIPS["default"])


def get_resources(subject):
    """Return a list of external resource links for the given subject."""
    key = _normalize(subject)
    return RESOURCES.get(key, RESOURCES["default"])


def display_help_for_weak_subjects():
    """Find the worst-performing subject and display tips and resources for it."""
    subject = get_worst_subject()

    print("\n--- Help for Weak Subjects ---")
    if subject is None:
        print("No sessions logged yet. Log some sessions to get personalized tips!")
        return

    print(f"📉 Your lowest-scoring subject is: {subject}")

    tips = get_tips(subject)
    print(f"\n💡 Study Tips for {subject.title()}:")
    for i, tip in enumerate(tips, 1):
        print(f"  {i}. {tip}")

    resources = get_resources(subject)
    print(f"\n🔗 Helpful Resources for {subject.title()}:")
    for resource in resources:
        print(f"  - {resource}")
