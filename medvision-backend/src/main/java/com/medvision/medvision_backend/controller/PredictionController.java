package com.medvision.medvision_backend.controller;

import com.medvision.medvision_backend.dto.PredictionResponseDTO;
import com.medvision.medvision_backend.dto.PredictionHistoryDTO;
import com.medvision.medvision_backend.service.PredictionService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import java.util.List;

@CrossOrigin(origins="*")
@RestController
@RequestMapping("/api/predictions")
@RequiredArgsConstructor
public class PredictionController {

    private final PredictionService predictionService;
    
    @PostMapping(consumes = "multipart/form-data")
    public PredictionResponseDTO predict(@RequestParam("file") MultipartFile file) throws Exception{
        return predictionService.analyzeImage(file);
    }

    @GetMapping
    public List<PredictionHistoryDTO> getPredictionHistory(){
        return predictionService.getAllPredictions();
    }
}

