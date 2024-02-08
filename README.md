# Sacrament Meeting Prayers Helper
An automated way to send weekly text messages

## Motivation
I am currently volunteering as a secretary to my church congregation's bishop. As part of my responsibilities, I am asked to find members of the congregation to give prayers at the beginning and end of our church worship services. I have a pretty poor track record.

After thinking about James Clear's book __Atomic Habits__, I decided to give this method a try of making things easier. It should take the guess work out of asking people. I don't have to think about who to ask, and this should make it loads faster to send messages.

## Usage
1. Sign in to churchofjesuschrist.org
2. create a report of members. Make sure to include `preferred name` and `individual phone`. I filtered down our ward directory by members with callings
3. Copy the output and paste it into `list-of-people.tsv`. It should be a tab separated file.
4. (optional) add preferred names to the `exclude-list.txt`. One name per line
5. Run the `create-schedule.py` script. It only uses vanilla python packages, so it should be easy to run
6. Set up the [iOS shortcut](https://www.icloud.com/shortcuts/11b4685f4c9b4190a3eea4c41ffa9056)
7. Make sure to update the shortcut to reach your specified file path to `schedule.json`. I put mine in iCloud to make it easier.
8. Run the shortcut

## Other
Please let me know if you find this useful or if you think this could be extended to your usecase.