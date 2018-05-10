import { Component } from '@angular/core';
import { StudentAuthenticationService } from './../student/student.authentication.service';
import { Observable } from 'rxjs/Observable';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { TokenPayload } from './../student/student';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  providers: [StudentAuthenticationService]
})

export class LoginComponent {
  title = 'Login';
  credentials: TokenPayload = {
    mail: '',
    password: ''
  };

  constructor(private auth: StudentAuthenticationService, private router: Router) { }
  login() {
    this.auth.login(this.credentials).subscribe(() => {
      this.router.navigateByUrl('/profile');
    }, (err) => {
      console.error(err);
    });
  }
}


