# Assignment1 - Practice Designing Models (Template)

> * Participant name: Ryan Fatt
> * Project Title: Urban Street Planning in a Smart City
## General Introduction

A **smart city** is an urban area that uses different types of electronic data collection sensors to supply information which is used to manage assets and resources efficiently.

![Image of Smart City](images/smartcity.png)

A major problem in many large cities is planning how to place streets to allow traffic to move efficiently while not cutting into neighborhoods.
According to an article by Ben Plowden there are two main uses for streets: moving and living. Being able to move goods through a city and getting from point A to point B are essential to the economy of every city.
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

Experiments would attempt to learn either a Interactive Dynamic Influence Diagram using structure learning
## Smart City (My Problem) Model

This model describes three types of agents can be categorized: vehicle agents which can include everything from a smart car to a delivery truck, pedestrians which includes anyone on the sidewalks and leisure agents which can include 
everything from food carts to street performers. Each of these agents acts differently but is informed by a communal IDID model. The IDID model will learn how to coordinate all 3 types of agents to provide the most efficient
solution to congestion possibl. This would ideally use structure learning from simulation data and eventually real-world data but it would be seeded with an initial state that will be shown here. 

(remove: Look at the [**Object Diagram**](model/object_diagram.md) for how to structure this part of Part 2 for each diagram. Only the Object diagram has the template, the rest are blank. )

* [**Object Diagram**](model/object_diagram.md) - provides the high level overview of components
* [**Class Diagram**](model/class_diagram.md) - provides details of (what are you providing details of)
* [**Behavior Diagram**](model/behavior_diagram.md) - provides details of (what are you providing details of)
* [**Agent / User case** (if appropriate)](model/agent_usecase_diagram.md) - provides details of the three types of agents.

## Smart City (My Problem) Simulation

(remove: for part 3 add two to three sentences here and link the [**(your own name)**](model/README.md) file in the analysis folder - which describe how you would simulate this - type of simulation, rough details -inputs, outputs - how it will help you analyze your experimental hypothesis, or nullify your null hypothesis.)


## Smart City (My Problem) Model
[**Code template**](code/README.md) - Starting coding framework for the (insert your exact problem here.)

## **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model
Here [**we provide an overview**](code/POTS_system/README.md) of the **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model and provide a source code template.
