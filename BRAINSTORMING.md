# Brainstorming.md

## Phase 0

**Problem:** The possible landing sites on the Moon (especially the Artemis targeted lunar South Pole) are too many and the factors needed to be taken into consideration are too many for each mission to be all studied by hand by scientists and engineers in a fast and scalable pace.

The scope of the project could be to launch a swarm of agents in a selected target area that analyze terrain safety and perform a mission simulation in different (but partially specified) time frames, in order to find the best candidates to serve for lunar landing for a given mission target. The agents act like sentinels that analyze all the terrain inside a specific user specified domain and move inside their assigned territory (based on terrain score given by a scorer) to find the best terrain which will be then evaluated by a super scorer. In every iteration the worst performance sentinels will be moved to the best candidates in order to have a finer analysis of the best candidates. The final output is a tiny fraction of possible candidates which will be scored by the super scorer. The terrain scorer is only aware of safety constrains and visibility constrains, whereas the super scorer is also aware of mission design constrains (inserted by the user into a MISSION.md instruction file). The framework is based on an agent + sentinel setup: each agent downloads from the LOLA database it's assigned terrain patch and performs educated guesses on the site condition based on Sun and Earth ephemerides calculated through JPL Horizons (or similar ephemerides tool) based on the need of the sentinel; the sentinel then maps the terrain and gives the result to a scorer that assign a score, based on the score the sentinel decides where to move and the process repeat. the sentinel can ask the agent to perform calculation in order to better evaluate how to move inside the site. when the iterations end the super scorer give each agent+sentinel a scorer and it moves the worst performance ones to best performance sites

The shape of the tool is still to be defined, i was thinking about a fast cli with a graphic interface to be called by the user. all backend is written in python

The agents should:

- analyze terrain slope and soil composition to evaluate feasibility for a landing and terrain activities
- evaluate best candidates that blend almost always illuminated areas (for solar panels) an almost always dark areas (for possible ice deposits)
- evaluate best candidates for earth and other orbiters visibility for relay and telecomms
- (tbd) evaluate site based on user specified mission targets

**Milestones:**

- study the feasibility of an agent base mission analysis framework
- study the possibility of using terrain reconstruction and interpolation algorithms
- understand how RL works and the scorer parameters
- define a primarily scoring method for each site
