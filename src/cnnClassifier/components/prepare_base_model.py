import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        """
        Initializes the PrepareBaseModel class with the provided configuration.

        Args:
            config (PrepareBaseModelConfig): Configuration for preparing the base model.
        """
        self.config = config

    def get_base_model(self):
        """
        Loads the VGG16 model with specified configurations and saves it.

        Actions:
            - Loads the VGG16 model with specified image size, weights, and top layer inclusion.
            - Saves the model to the path specified in the configuration.
        """
        # Load the VGG16 model using specified parameters
        self.model = tf.keras.applications.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )

        # Save the loaded base model
        self.save_model(path=self.config.base_model_path, model=self.model)

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        """
        Prepares the full model by adding a classification layer on top of the base model.

        Args:
            model (tf.keras.Model): The base model to be extended.
            classes (int): Number of output classes (update to 3).
            freeze_all (bool): Whether to freeze all layers of the base model.
            freeze_till (int): Number of layers from the end of the model to be unfrozen.
            learning_rate (float): Learning rate for the optimizer.

        Returns:
            tf.keras.Model: The full model with a classification head.
        """
        # Freeze layers based on the freeze_all and freeze_till parameters
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False

        # Add a new classification layer on top of the base model
        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,  # Set to 3 for three classes
            activation="softmax"
        )(flatten_in)

        # Create a new model with the updated top layer
        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        # Compile the model
        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),  # Use SparseCategoricalCrossentropy if using integer labels
            metrics=["accuracy"]
        )

        # Print the model summary
        full_model.summary()
        return full_model

    def update_base_model(self):
        """
        Updates the base model by preparing it for classification and saving the updated model.

        Actions:
            - Prepares the full model by adding a classification head.
            - Saves the updated model to the path specified in the configuration.
        """
        # Prepare the full model with the classification head
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,  # Update to 3 for three classes
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        # Save the updated model
        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        """
        Saves the model to the specified path.

        Args:
            path (Path): Path to save the model.
            model (tf.keras.Model): Model to be saved.
        """
        model.save(path)