import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule, Http } from '@angular/http';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { LoginComponent } from './login/login.component';
import { RouterModule, Routes } from '@angular/router';
import { PageNotFoundComponent } from './pagenotfound.component';
import { HttpClientModule } from '@angular/common/http';

const appRoutes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: '**', component: PageNotFoundComponent }
];

@NgModule({
  declarations: [
    AppComponent, LoginComponent, PageNotFoundComponent
  ],
  imports: [
    BrowserModule, HttpModule, FormsModule, RouterModule.forRoot(appRoutes), HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
