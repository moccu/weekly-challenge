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
import Foundation

extension Array {
    mutating func popFirst() -> Element {
        let firstChild = self.first!
        self.removeFirst()
        return firstChild
    }
}

let teams: [String] = [
    "Hertha BSC", "1. FSV Mainz 05", "Borussia Mönchengladbach", "FC Augsburg", "Hannover 96", "Bayer 04 Leverkusen",
    "FC Ingolstadt 04", "SV Werder Bremen", "Borussia Dortmund", "TSG 1899 Hoffenheim", "1. FC Köln", "Hamburger SV",
    "Eintracht Frankfurt", "FC Bayern München", "VfB Stuttgart", "VfL Wolfsburg", "FC Schalke 04", "SV Darmstadt 98",
]
let teamsCount: Int = teams.count/2
var matchPlan: [[[String]]] = []

func calcMatches(var teams1: [String], var teams2: [String]) -> [[String]] {
    var matchDay: [[String]] = []

    teams2.append(teams1.popLast()!)
    teams1.insert(teams2.popFirst(), atIndex: 1)

    for i in 0...teams1.count-1 {
        matchDay.append([teams1[i], teams2[i]])
    }

    if (!(teams1 + teams2).elementsEqual(teams)) {
        calcMatches(teams1, teams2: teams2)
    }
    
    matchPlan.append(matchDay)
    
    return matchDay
}

calcMatches(Array(teams.prefix(teamsCount)), teams2: Array(teams.suffix(teamsCount)))

for (index,day) in matchPlan.enumerate() {
    print("Spieltag: \(index+1)")
    for match in day {
        print("\(match[0]) - \(match[1])")
    }
    print("\n")
}
```
From: Martin | Language: Swift

---

```python
def build_tournament(teams):
    if len(teams) % 2 != 0:
        teams.append('-')

    num_teams = len(teams)
    rounds = [
        [teams[0]] + teams[num_teams - day:] + teams[1:num_teams - day]
        for day in range(0, num_teams - 1)
    ]

    for num, teams in enumerate(rounds, 1):
        print('\nRound {0}'.format(num))
        while teams:
            print('- {0} vs {1}'.format(teams.pop(0), teams.pop(-1)))
```
From: Stephan | Language: Python
