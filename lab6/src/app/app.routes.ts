import { Routes } from '@angular/router';
import { FirstComponent } from './components/first/first.component';
import { SecondComponent } from './components/second/second.component';

export const routes: Routes = [
{path : '' , redirectTo: 'first' , pathMatch : 'full'},
{path : 'first' , component : FirstComponent} ,
{path : 'second', component : SecondComponent}

];
