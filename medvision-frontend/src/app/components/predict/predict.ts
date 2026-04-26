import { Component, inject, signal } from '@angular/core';

import { Prediction } from '../../services/prediction';
import {FileUploadModule} from 'primeng/fileupload';
import { ProgressBarModule } from 'primeng/progressbar';
import { DecimalPipe } from '@angular/common';
import {TagModule} from 'primeng/tag';
 
@Component({
  selector: 'app-predict',
  imports: [FileUploadModule,
      ProgressBarModule,
      DecimalPipe,
      TagModule,
  ],
  templateUrl: './predict.html',
  styleUrl: './predict.css',
})
export class Predict {
 result=signal<any>(null);

  private predictionService = inject(Prediction);

  onUpload(event:any){
    const file = event.files[0];
    this.predictionService.Predict(file).subscribe(res=>{
      this.result.set(res);
      
    })
  }



}
