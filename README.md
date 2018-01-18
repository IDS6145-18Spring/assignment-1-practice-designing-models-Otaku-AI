# Assignment1 - Practice Designing Models (Template)

> * Participant name: Ryan Fatt
> * Project Title: Urban Street Planning in a Smart City
## General Introduction

A **smart city** is an urban area that uses different types of electronic data collection sensors to supply information which is used to manage assets and resources efficiently.

![Image of Smart City](images/smartcity.png)

A major problem in many large cities is planning how to place streets to allow traffic to move efficiently while not cutting into neighborhoods.
According to an article by Ben Plowden (https://nextcity.org/daily/entry/problem-urban-street-planning-london-walkability-cars) there are two main uses for streets: moving and living. Being able to move goods through a city and getting from point A to point B are essential to the economy of every city.
The other major role of streets is to provide a place for civic life to play out. Everything from street performances to enjoying a nice day at a sidewalk cafe are essential goals of city streets.
According to Plowden the focus on living has been mostly ignored in exchange for moving ever since World War 2. This is only set to get worse as traffice congestion increases
Proposed solutions to urban planning mostly include city task forces which have developed models classifying the functions and needs of streets. However, a smart city could expand these options by providing the ability to adapt to the 
current situation instead of having to be statically planned in advance.

## Requirements (Experimental Design)
Null Hypothesis: Sensors and intelligent agents have no ability to alleviate congestion and crowding on city streets.

Alternative Hypothesis: Sensors and intelligent agents can aleviate congestion and crowding on city streets.

I hypothesize that using a variety of sensors combined with methods taken from the study of multiagent systems can be used to help alleviate congestion. 
Sensors used would include motion sensors to sense where people are gathered as well as camera systems that utilize optical flow to determine the rate of movement through an areas sidewalks. 
Traffic camera systems can be used to accomplish the same thing with vehicles. Other sensors could attempt to model emotional state of citizens using wearables for pulse and camera systems for facial expression recognition though
this may not be desirable due to privacy concerns.

Experiments would attempt to learn the parameters for an interactive dynamic influence diagram (http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.113.6492&rep=rep1&type=pdf) and to classify sensor patterns for future predictions and user personalities using bayesian networks (https://www.cs.ubc.ca/~murphyk/Bayes/bnintro.html).
## Smart City Street Congestion Model

This model describes three types of agents can be categorized: vehicle agents which can include everything from a smart car to a delivery truck, pedestrians which includes anyone on the sidewalks and leisure agents which can include 
everything from food carts to street performers. Each of these agents acts differently but is informed by a communal IDID model. The IDID model will learn how to coordinate all 3 types of agents to provide the most efficient
solution to congestion possibl. This would ideally use structure learning from simulation data and eventually real-world data but it would be seeded with an initial state that will be shown here. 

[**Object Diagram**](model/object_diagram.md) - provides the high level overview of components.

[**Agent Class Diagram**](model/agent_diagram.md) - provides details of each type of agent.

[**Sensor Class Diagram**](model/sensor_diagram.md) - provides details of each type of sensor.

[**PGM Diagram**](model/pgm_diagram.md) - provides details of the probabilistic graphical models.

[**Behavior Diagram**](model/behavior_diagram.md) - provides details of how each part of the system interactions with the bayesian inference systems.

[**Agent / User case** (if appropriate)](model/agent_usecase_diagram.md) - provides details of how each type of agent would use the system.

## Smart City Street Congestion Simulation

I would use agent based simulation to solve this problem. I would build a virtual model of the city in Unreal Engine and program agent behavior to allow the simulation to play out automatically. This would provide at least some experimental data to train the bayesian networks on. You can read more about my [**simulation plan**](analysis/README.md) by clicking the link


## Smart City Street Congestion Model
You can find some of the agent classes here: [**Agent Classes**](code/streetcongestion)

## **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model
Here [**we provide an overview**](code/POTS_system/README.md) of the **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model and provide a source code template.
