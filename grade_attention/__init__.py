"""
GRADE Attention v2 — Production System
Gravitational + Wave + Linear + MoE Attention for Sovereign Local AI (Victor)
"""

from .grade_v2 import (
    GradeAttention,
    GradeWaveAttention,
    LinearGradeAttention,
    HybridAttentionRouter,
    MixtureOfGradeExperts,
    DynamicGradeBlock,
    load_balancing_loss,
)

__all__ = [
    "GradeAttention",
    "GradeWaveAttention",
    "LinearGradeAttention",
    "HybridAttentionRouter",
    "MixtureOfGradeExperts",
    "DynamicGradeBlock",
    "load_balancing_loss",
]

__version__ = "2.5.0"