from roboflow import Roboflow
rf = Roboflow(api_key="")
project = rf.workspace("tushar-sethi-svpyx").project("ai-based-ocean-plastic-detection")
version = project.version(2)
dataset = version.download("yolov8")