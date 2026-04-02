# RAKSHA Entity Profiler
> OSINT Project 01 | RAKSHA Defense Intelligence Platform

## What This Does
A CLI-based OSINT entity profiling tool that collects, structures, and validates 
intelligence data on threat actors — individuals, organizations, or locations. 
Generates a formatted Intelligence Brief and maintains a live Watchlist across 
a session.

## Why It Exists
Defense and intelligence workflows require structured, repeatable processes for 
threat actor documentation. This tool simulates the data intake layer of a 
real-world OSINT pipeline — converting raw field inputs into structured 
intelligence profiles with threat scoring, confidence weighting, and source 
verification.

Built as the first technical component of RAKSHA — an AI-powered OSINT and 
defense intelligence platform being developed for India's national security 
ecosystem.

## Features
- Multi-entity profiling in a single session
- Threat scoring (0–100) with confidence weighting (0.0–0.9)
- Active/Inactive status tracking
- Alias mapping and geospatial coordinate intake
- Source URL logging with verification flag
- Real-time data type validation
- Session-level Watchlist with summary output

## Tech Stack
- Python 3.x
- No external dependencies — pure standard library

## How to Run
```bash
python raksha_entity_profiler.py
```
Follow the CLI prompts to input entity data. At the end of the session, 
a Watchlist Summary is displayed ranking all profiled entities by threat score.

## Sample Output
```
--- INTELLIGENCE BRIEF ---
Entity     : Lashkar-e-Taiba
Type       : Organization
Category   : Terrorism
Threat Score: 91/100
Confidence : 0.9
Status     : ACTIVE
Aliases    : LeT, JuD
Area of Interest: Kashmir, Punjab
Coordinates: (34.0837, 74.7973)
Source     : [redacted]
Verified   : YES
```

## About RAKSHA
RAKSHA is an AI-powered OSINT and defense intelligence platform being built 
for India's national security ecosystem — targeting threat actor profiling, 
border intelligence, and critical infrastructure surveillance.

Currently pursuing iDEX/DISC recognition under India's Ministry of Defence.

---
*Project 01 of an ongoing technical build. More modules in development.*
