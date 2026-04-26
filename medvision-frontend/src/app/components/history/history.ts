import { Component, inject, signal, OnInit } from '@angular/core';
import { Table, TableModule } from 'primeng/table';
import { Prediction } from '../../services/prediction';
import {DecimalPipe,DatePipe} from '@angular/common';
import { TagModule } from 'primeng/tag';
import {DialogModule} from 'primeng/dialog';
import { ButtonDirective } from "primeng/button";

@Component({
  selector: 'app-history',
  imports: [TableModule,
    DecimalPipe,
    TagModule,
    DatePipe,
    DialogModule, ButtonDirective],
  templateUrl: './history.html',
  styleUrl: './history.css',
})
export class History implements OnInit {
result=signal<any>(null);
dialogvisible=signal(false);
imagesrc?:string;
  private predictionService = inject(Prediction);
    ngOnInit(){
    this.predictionService.getHistory().subscribe(res=>{
      this.result.set(res);
      
    })
  }

  openHeatmap(url:string){
         this.imagesrc='http://localhost:8080' + url;
         this.dialogvisible.set(true);
  }


}
