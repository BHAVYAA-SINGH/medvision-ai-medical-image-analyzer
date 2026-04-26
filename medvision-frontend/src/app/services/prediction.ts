import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})


export class Prediction {
  constructor(private http:HttpClient){}

 api="http://localhost:8080/api/predictions";

 Predict(file:File):Observable<any>{
  const formData=new FormData();
  formData.append('file',file);
    return this.http.post<any>(this.api,formData);
  }

  getHistory():Observable<any> {
    return this.http.get<any> (this.api);
  }
}
