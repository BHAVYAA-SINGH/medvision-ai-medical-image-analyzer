package com.medvision.medvision_backend.client;

import com.medvision.medvision_backend.dto.AiResponseDTO;
import lombok.RequiredArgsConstructor;
// import org.springframework.core.io.FileSystemResource;
import org.springframework.http.MediaType;
import org.springframework.http.client.MultipartBodyBuilder;
import org.springframework.stereotype.Component;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.core.io.ByteArrayResource;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
@Component
@RequiredArgsConstructor
public class AiClient {

    private final WebClient webClient;

    public AiResponseDTO sendToAI(String filePath)  throws IOException{
        byte[] fileContent = Files.readAllBytes(Paths.get(filePath));
        MultipartBodyBuilder builder =new MultipartBodyBuilder();
        builder.part("file",new ByteArrayResource(fileContent)).filename("upload.jpg");

        return webClient.post()
               .uri("/predict")
               .contentType(MediaType.MULTIPART_FORM_DATA)
               .bodyValue(builder.build())
               .retrieve()
               .bodyToMono(AiResponseDTO.class)
               .block();
    }
    
}
