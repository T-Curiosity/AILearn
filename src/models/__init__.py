"""
模型定义模块
"""

from typing import Any, Dict, List, Optional
from abc import ABC, abstractmethod


class BaseModel(ABC):
    """模型基类"""
    
    def __init__(self, name: str):
        self.name = name
        self.is_trained = False
        self.model = None
        
    @abstractmethod
    def train(self, X_train: Any, y_train: Any) -> None:
        """训练模型"""
        pass
    
    @abstractmethod
    def predict(self, X: Any) -> Any:
        """预测"""
        pass
    
    @abstractmethod
    def evaluate(self, X_test: Any, y_test: Any) -> Dict[str, float]:
        """评估模型"""
        pass
    
    def save_model(self, filepath: str) -> None:
        """保存模型"""
        import pickle
        with open(filepath, 'wb') as f:
            pickle.dump(self.model, f)
    
    def load_model(self, filepath: str) -> None:
        """加载模型"""
        import pickle
        with open(filepath, 'rb') as f:
            self.model = pickle.load(f)
        self.is_trained = True


class MLModel(BaseModel):
    """机器学习模型类"""
    
    def __init__(self, name: str, model_type: str = "sklearn"):
        super().__init__(name)
        self.model_type = model_type
    
    def train(self, X_train: Any, y_train: Any) -> None:
        """训练模型"""
        if self.model is None:
            raise ValueError("模型未初始化")
        
        self.model.fit(X_train, y_train)
        self.is_trained = True
    
    def predict(self, X: Any) -> Any:
        """预测"""
        if not self.is_trained:
            raise ValueError("模型未训练")
        
        return self.model.predict(X)
    
    def evaluate(self, X_test: Any, y_test: Any) -> Dict[str, float]:
        """评估模型"""
        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
        
        predictions = self.predict(X_test)
        
        return {
            "accuracy": accuracy_score(y_test, predictions),
            "precision": precision_score(y_test, predictions, average='weighted'),
            "recall": recall_score(y_test, predictions, average='weighted'),
            "f1": f1_score(y_test, predictions, average='weighted')
        }
