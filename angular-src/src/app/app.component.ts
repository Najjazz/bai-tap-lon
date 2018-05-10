import { Component, Input } from '@angular/core';
declare var require: any;
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
// This is require because we need an absolute path of image at run time
private STUDENT_LOGO = require('./login/img/c1.png');
private LECTURER_LOGO = require('./login/img/c2.png');
private ENTERPRISE_LOGO = require('./login/img/c3.png');

}
