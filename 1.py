from graphviz import Digraph

# Create a new Digraph (graph object)
dot = Digraph()

# Define the activities
activities = [
    'Start',
    'Capture image',
    'Preprocess image',
    'Extract features',
    'Analyze features',
    'Emotion prediction',
    'Display emotion',
    'End'
]

# Add nodes to the graph
for activity in activities:
    if activity == 'Start' or activity == 'End':
        dot.node(activity, shape='circle')
    elif activity == 'Analyze features':
        dot.node(activity, shape='diamond')
    else:
        dot.node(activity, shape='box')

# Define the connections between activities
connections = [
    ('Start', 'Capture image'),
    ('Capture image', 'Preprocess image'),
    ('Preprocess image', 'Extract features'),
    ('Extract features', 'Analyze features'),
    ('Analyze features', 'Emotion prediction'),
    ('Emotion prediction', 'Display emotion'),
    ('Display emotion', 'End')
]

# Add edges to the graph
for connection in connections:
    dot.edge(*connection)

# Render the graph as a PNG image
dot.format = 'png'
dot.render('facial_emotion_recognition_activity_diagram', view=True)
