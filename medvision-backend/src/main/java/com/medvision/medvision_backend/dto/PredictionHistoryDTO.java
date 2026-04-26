package com.medvision.medvision_backend.dto;

import lombok.Builder;
import lombok.Data;
import java.time.LocalDateTime;

@Data
@Builder
public class PredictionHistoryDTO {
    private Long id;
    private String prediction;
    private double confidence;
    private String modelVersion;
    private String heatmapUrl;
    private LocalDateTime createdAt;
    
}
