"""The practice file for group 110"""
# Edit by Yushen An


nom = [
    ("Andre Robinson", "Great coworker", 94),
    ("Sandra Jimenez", "Extra mile", 96),
    ("Olivia Smith", "Great coworker", 99),
    ("Vernon Jones", "Extra mile", 92),
    ("Wally Yamamoto", "Extra mile", 97)
]

def winner(nom):
    """Function that checks the winner in each category
        Returns:
            returns the result
        Args: takes in nom which is a list of tuples
    """
    
    winners = {}
    for name, category, score in nom:
        if category not in winners or score > winners[category][1]:
            winners[category] = (name,score)
    return {category: name for category,(name,score) in winners.items()}

print(winner(nom))

# Edit by Adib Aayan:
print("Total nominations:", len(nom))
print("Categories:", {c for _, c, _ in nom})
print("Highest overall score:", max(nom, key=lambda x: x[2]))
