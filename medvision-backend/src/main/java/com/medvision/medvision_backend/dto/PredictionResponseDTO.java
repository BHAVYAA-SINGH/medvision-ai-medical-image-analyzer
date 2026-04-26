package com.medvision.medvision_backend.dto;

import lombok.Data;

@Data
public class PredictionResponseDTO {
    private String prediction;
    private double confidence;
    private String heatmapPath;
    private String modelVersion;
    
}
