## Smart City Street Congestion Model

In the POIS_system folder I have added my object and class diagrams for the POTS system

In the street congestion folder I implemented the agent class and its 3 main subclasses: vehicle pedestrian and leisure.

The  [**agent class**](streetcongestion/agent.py)   has the general functionality for an agent such as sending and receiving messages and having plans and priorities that the system assigns.

The [**vehicle class**](streetcongestion/Vehicle.py)  has the basic functionality to allow cars to give and accept new directions.

The [**pedestrian class**](streetcongestion/Pedestrian.py) implements pedestrians personality and motivation and current plans and allows querying into the system.

The [**leisure class**](streetcongestion/leisure.py) provides the basic functionality to allow a leisure agent to advertise and use the system to their businesses advantag
