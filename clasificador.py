from pysentimiento import create_analyzer

class EmotionAnalyzer:
    """
    Clase para analizar el estado de ánimo del usuario usando NLP avanzado.
    """

    def __init__(self):
        """Inicializa el analizador con el modelo pre-entrenado en español."""
        self.analyzer = create_analyzer(task="emotion", lang="es")

    def predict_emotion(self, text):
        """
        Predice la emoción del texto ingresado por el usuario.

        Args:
            text (str): Texto del usuario.

        Returns:
            str: Categoría de estado de ánimo.
        """
        result = self.analyzer.predict(text)
        return self._map_emotion(result.output)

    def _map_emotion(self, emotion):
        """
        Mapea las emociones del modelo a categorías personalizadas.

        Args:
            emotion (str): Emoción detectada por el modelo.

        Returns:
            str: Categoría de estado de ánimo personalizada.
        """
        emotion_map = {
            'joy': 'Alegre',
            'surprise': 'Alegre',
            'sadness': 'Melancólico',
            'anger': 'Melancólico',
            'fear': 'Melancólico',
            'disgust': 'Melancólico',
            'neutral': 'Ni fu ni fa',
            'others': 'Ni fu ni fa'
        }
        print(emotion)
        return emotion_map.get(emotion, "Desconocido")

# Ejemplo de uso
if __name__ == "__main__":
    analyzer = EmotionAnalyzer()
    text = input("Ingrese un texto: ")
    mood = analyzer.predict_emotion(text)
    print(f"Estado de ánimo detectado: {mood}")
