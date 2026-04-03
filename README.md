**Adaptive Travel Planner RL Environment**



&#x20;*Description*



This project is a reinforcement learning environment designed to simulate a real-world travel planning scenario.

In this system, an agent selects travel destinations, and each decision is evaluated based on factors such as user preferences, available budget, place quality, and user satisfaction.





&#x20;*Idea Behind the Project*



The purpose of this environment is to represent how people make travel decisions in real life.

Instead of fixed answers, the system gives feedback in the form of rewards, helping an agent understand which choices are better over time.





*Environment Design*



State



The environment provides the following information to the agent:



\* Budget: the remaining money available for travel

\* Preferences: user interests such as nature or spiritual places

\* Day: the current day of the trip





Actions



The agent can choose one of the following options:



\* 0: Goa Beach (nature, higher cost, good rating)

\* 1: Tirupati Temple (spiritual, moderate cost, excellent rating)

\* 2: City Park (nature, low cost, average rating)



Reward Design



The reward function is created to reflect real-world decision quality.

The agent receives rewards based on:



\* Matching the user’s preferences

\* Staying within the available budget

\* The rating or quality of the selected place

\* Simulated user response (whether the user is satisfied or not)



This combination ensures that the agent is encouraged to make balanced and realistic decisions.





*Environment Behavior*



Each run of the environment represents a short trip:



\* The trip lasts for three steps (days)

\* The agent selects one action per step

\* The budget and day are updated after each decision

\* The process ends after three steps





&#x20;*Tasks*



The environment includes three levels of tasks:



Easy



\* Focuses on making a single good recommendation



Medium



\* Involves planning for two steps while considering budget



Hard



\* Requires planning a complete three-step trip while balancing all factors



The performance is measured using a score between 0 and 1.





&#x20;*Baseline Agent*



A simple agent is included to interact with the environment.

It helps demonstrate how the environment works, but it is not optimized or trained.



How to Run



Run the following files:



python test\_env.py

python agent.py

python evaluate.py



*Requirements*



Python 3.x



*Key Features*



\* Dynamic preferences that change across runs

\* Variable budget to simulate different users

\* Reward system based on multiple real-world factors

\* Simulation of user satisfaction





*Conclusion*



This project provides a structured environment where reinforcement learning agents can be tested on travel planning decisions.

It focuses on realistic constraints and user behavior, making it suitable for experimentation and further improvements.



