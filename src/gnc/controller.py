class GNController:
    def __init__(self, tracker, detector):
        self.tracker = tracker
        self.detector = detector
    
    def avoid_debris(self, image_path):
        """Pipeline complet GNC"""
        debris_list = self.detector.detect(image_path)
        current_pos = self.tracker.kf.x[0]
        
        for debris in debris_list:
            if debris['confidence'] > 0.9:  # Seuil de confiance
                return current_pos * 1.2  # Manœuvre d'évitement
        return current_pos