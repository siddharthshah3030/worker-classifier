
from imageai.Prediction.Custom import ModelTraining

model_trainer = ModelTraining()
model_trainer.setModelTypeAsResNet()
model_trainer.setDataDirectory("idenprof")

model_trainer.trainModel(num_objects=2, num_experiments=1, enhance_data=False, batch_size=5, show_network_summary=True)
