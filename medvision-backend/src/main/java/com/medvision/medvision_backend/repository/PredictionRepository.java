package com.medvision.medvision_backend.repository;

import com.medvision.medvision_backend.entity.PredictionRecord;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PredictionRepository extends JpaRepository<PredictionRecord,Long> {
    
}
