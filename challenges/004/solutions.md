# 004: Round Robin Tournament

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

Source:

---

```python
def tournament(teams):
    if len(teams) % 2:
        teams.append('Day off')

    tournament = []

    for i in range(0, len(teams) - 1):
        tournament.append(teams)
        teams = [teams[0]] + [teams[-1]] + teams[1:-1]
    return tournament

my_teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

my_tournament = tournament(my_teams)

i = 1
for day in my_tournament:
    print('Matches Day {0} of Tournament:'.format(i))
    while day:
        if day[0] == 'Day off':
            print(day[len(day) - 1] + ': Day off')

        elif day[len(day) - 1] == 'Day off':
            print(day[0] + ': Day off')

        else:
            print(day[0] + ' vs ' + day[len(day) - 1])

        day = day[1:-1]

    i += 1
```
From: Ute | Language: Python

---

```swift
let teams: [String] = [
    "Hertha BSC Berlin", "Borussia Dortmund", "FC Augsburg", "FC Bayern München", "Hamburger SV",
    "Werder Bremen", "1. FC Mainz 05", "Schalke 04", "Darmstadt", "Bayer 04 Leverkusen",
    "Hannover 96", "VfB Stuttgart", "1899 Hoffenheim", "VfL Wolfsburg", "FC Ingolstadt",
    "1. FC Köln", "Eintracht Frankfurt", "Borussia Mönchengladbach"]
let teamsCount: Int = teams.count/2
var matchPlan: [[[String]]] = []

func calcMatches(var teams1: [String], var teams2: [String]) -> [[String]] {
    var matchDay: [[String]] = []

    teams2.insert(teams1.popLast()!, atIndex: teams2.count)
    teams1.insert(teams2.first!, atIndex: 1)
    teams2.removeFirst()

    for i in 0...teams1.count-1 {
        matchDay.append([teams1[i], teams2[i]])
    }

    if (!(teams1 + teams2).elementsEqual(teams)) {
        matchPlan.append(calcMatches(teams1, teams2: teams2))
    }
    
    return matchDay
}

matchPlan.append(calcMatches(Array(teams.prefix(teamsCount)), teams2: Array(teams.suffix(teamsCount))))
```
from Martin | Language: Swift
