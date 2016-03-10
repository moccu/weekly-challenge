# 007: Regex for dates

Match dates in YYYY/MM/DD HH:MM(:SS) format with a regex. YYYY should be a year between 1000 and 2012, and everything else should be a valid month, date, hour, minute and second. The seconds should be optional. Don't worry about leap years, and assume that all months have 30 days.

You can find interactive test cases at [Regex Tuesday](http://callumacrae.github.io/regex-tuesday/challenge3.html).

Source: [Regex Tuesday](http://callumacrae.github.io/regex-tuesday/challenge3.html)

---

```javascript
(1\d{3}|20(0[0-9]|1[0-2]))\/(0[1-9]|1[0-2])\/(0[1-9]|1[0-9]|2[0-9]|30)\s(0[0-9]|1[0-2])\:([0-5]\d)(\:([0-5]\d))?
```
From: Dimitri

---

```javascript
^(1\d{3}|20(0\d|1[0-2]))\/(0[1-9]|1[0-2])\/(0[1-9]|[12]\d|30)\s([01]\d|2[0-3])\:([0-5]\d)(\:([0-5]\d))?$
````
From: Martin | Language: JavaScript

---

```javascript
(1\d{3}|20(0\d|1[0-2]))\/(0[1-9]|1[0-2])\/(0[1-9]|[1-2]\d|30)\s([0-1]\d|2[0-4])\:[0-5]\d(\:[0-5]\d)?
````
From: Jannik | Language: JavaScript
