-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Check crime scene reports for the date of the crime
SELECT description FROM crime_scene_reports
WHERE year = "2021" AND month = "07" AND day = "28";

-- Crime took place at 10:15 and three witnesses were interviewed on date of the crime
-- Check interviews on date of the crime
SELECT name, transcript FROM interviews
WHERE year = "2021" AND month = "07" AND day = "28";

-- Three witnesses (Ruth, Eugene, and Raymond) give different pieces of helpful information
-- 1) RUTH
-- Ruth saw the thief get into a car and drive away within 10 minutes of the crime.  Look at security footage
SELECT activity, license_plate FROM bakery_security_logs
WHERE year = "2021" AND month = "07" AND day = "28" AND hour = "10" AND minute >= "15" AND minute <= "25";

-- The security footage leads to 8 possible license plates of cars exiting
-- Match those license plates to the people list to find the names and numbers of 8 suspects
SELECT name FROM people
WHERE license_plate IN
(SELECT license_plate FROM bakery_security_logs
WHERE year = "2021" AND month = "07" AND day = "28" AND hour = "10" AND minute >= "15" AND minute <= "25");
-- This results in the names of 8 suspects

-- 2) EUGENE
-- Eugene said that the thief withdrew money from the ATM on Leggett Street earlier that morning
SELECT account_number FROM atm_transactions
WHERE atm_location = "Leggett Street" AND year = "2021" AND month = "07" AND day = "28";

-- The ATM search leads to 9 accounts, so link account numbers to person ids
SELECT person_id FROM bank_accounts
WHERE account_number IN
(SELECT account_number FROM atm_transactions
WHERE atm_location = "Leggett Street" AND year = "2021" AND month = "07" AND day = "28");

-- And then person ids to people
SELECT name FROM people
WHERE id IN
(SELECT person_id FROM bank_accounts
WHERE account_number IN
(SELECT account_number FROM atm_transactions
WHERE atm_location = "Leggett Street" AND year = "2021" AND month = "07" AND day = "28"));
-- This results in the names and numbers of 9 suspects

--3) RAYMOND
-- Raymond said that thief talked to an accomplice on the phone for less than a minute that day
-- and that they took the "earliest flight out of fiftyville"
SELECT caller FROM phone_calls
WHERE duration < "60" AND year = "2021" AND month = "07" AND day = "28";

-- This results in 9 numbers, so match to names
SELECT name FROM people
WHERE phone_number IN
(SELECT caller FROM phone_calls
WHERE duration < "60" AND year = "2021" AND month = "07" AND day = "28");

--COMBINE info from 1, 2, and 3 to find suspect's name
SELECT name FROM people
WHERE phone_number IN
(SELECT caller FROM phone_calls
WHERE duration < "60" AND year = "2021" AND month = "07" AND day = "28")
AND id IN
(SELECT person_id FROM bank_accounts
WHERE account_number IN
(SELECT account_number FROM atm_transactions
WHERE atm_location = "Leggett Street" AND year = "2021" AND month = "07" AND day = "28"))
AND license_plate IN
(SELECT license_plate FROM bakery_security_logs
WHERE year = "2021" AND month = "07" AND day = "28" AND hour = "10" AND minute >= "15" AND minute <= "25");

--The two possibilties are Diana and Bruce, so check to see which one took a flight on July 29
--First find flight IDs for July 29
SELECT id, hour, minute FROM flights
WHERE year = "2021" AND month = "07" AND day = "29";

--Then find names of people on flight 36, the earliest
SELECT name FROM people
WHERE passport_number IN
(SELECT passport_number FROM passengers
WHERE flight_id = "36");
--Bruce and not Diana is on this list, so Bruce is the suspect

--Use flight number to find city (which is NYC)
SELECT city FROM airports
WHERE id = (SELECT destination_airport_id FROM flights
WHERE id = "36");

--Finally, use nested phone data to find accomplice, who is Robin
SELECT name from people
WHERE phone_number =
(SELECT receiver from phone_calls
WHERE caller =
(SELECT phone_number FROM people
WHERE name = "Bruce")
AND duration < "60" AND year = "2021" AND month = "07" AND day = "28");