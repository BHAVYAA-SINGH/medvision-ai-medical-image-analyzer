package com.medvision.medvision_backend.service;

import com.medvision.medvision_backend.client.AiClient;
import com.medvision.medvision_backend.dto.AiResponseDTO;
import com.medvision.medvision_backend.dto.PredictionHistoryDTO;
import com.medvision.medvision_backend.repository.PredictionRepository;
import lombok.RequiredArgsConstructor;
import com.medvision.medvision_backend.dto.PredictionResponseDTO;
import com.medvision.medvision_backend.entity.PredictionRecord;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;
import java.util.stream.Collectors;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.LocalDateTime;
import java.util.Base64;
import java.util.List;

@Service
@RequiredArgsConstructor
public class PredictionService {
    private final PredictionRepository repository;
    private final AiClient aiClient;

    public PredictionResponseDTO analyzeImage(MultipartFile file) throws IOException {
        File temp = File.createTempFile("upload_", ".jpg");
        try{  
        file.transferTo(temp);
        AiResponseDTO aiResult=aiClient.sendToAI(temp.getAbsolutePath());
        PredictionResponseDTO response = new PredictionResponseDTO();
        String heatmapUrl=saveHeatmap(aiResult.getHeatmap_image());
        PredictionRecord record = new PredictionRecord();
        record.setPrediction(aiResult.getPrediction());
        record.setConfidence(aiResult.getConfidence());
        record.setModelVersion(aiResult.getModel_version());
        record.setHeatmapUrl(heatmapUrl);
        record.setCreatedAt(LocalDateTime.now());
        repository.save(record);
        response.setPrediction(aiResult.getPrediction());
        response.setConfidence(aiResult.getConfidence());
        response.setModelVersion(aiResult.getModel_version());
        response.setHeatmapPath(heatmapUrl);
        return response;
        }finally{
            temp.delete();
        }
    }

    private String saveHeatmap(String base64Image) throws IOException {
        byte[] imageBytes=Base64.getDecoder().decode(base64Image);
        String filename="heatmap_" + System.currentTimeMillis() + ".jpg";
        Path path =Path.of("medvision-storage/heatmaps/" + filename);
        Files.write(path,imageBytes);
        return "/files/heatmaps/" + filename;
    }

    public List<PredictionHistoryDTO> getAllPredictions(){
        return repository.findAll()
        .stream()
        .map(record->PredictionHistoryDTO.builder()
        .id(record.getId())
        .prediction(record.getPrediction())
        .confidence(record.getConfidence())
        .modelVersion(record.getModelVersion())
        .heatmapUrl(record.getHeatmapUrl())
        .createdAt(record.getCreatedAt())
        .build())
        .collect(Collectors.toList());
    }
}
