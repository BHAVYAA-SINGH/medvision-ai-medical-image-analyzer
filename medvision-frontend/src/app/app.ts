import { Component, signal } from '@angular/core';
import { RouterOutlet, RouterLinkWithHref } from '@angular/router';
import {MenubarModule} from 'primeng/menubar';


@Component({
  selector: 'app-root',
  imports: [RouterOutlet, MenubarModule, RouterLinkWithHref],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('medvision-frontend');
}
