import { Routes } from '@angular/router';
import { Predict } from './components/predict/predict';
import {History} from './components/history/history';
import { About } from './components/about/about';


export const routes: Routes = [
    {path:'', redirectTo:'predict', pathMatch:'full'},
    {path:'predict',component:Predict},
    {path:'history',component:History},
    {path:'about',component:About},
];
