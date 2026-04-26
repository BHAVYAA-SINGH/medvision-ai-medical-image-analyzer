package com.medvision.medvision_backend.dto;

import lombok.Data;

@Data
public class AiResponseDTO {
    private String prediction;
    private double confidence;
    private String model_version;
    private String heatmap_image;
    
}
