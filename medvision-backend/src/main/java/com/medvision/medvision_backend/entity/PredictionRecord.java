package com.medvision.medvision_backend.entity;

import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDateTime;

@Entity
@Data
public class PredictionRecord { 
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String prediction;
    private double confidence;
    private String modelVersion;
    private String heatmapUrl;
    private LocalDateTime createdAt;
}
