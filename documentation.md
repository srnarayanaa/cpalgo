<details>
    <h1 style="display:inline-block"><summary>Advanced Topics</summary></h1>
    
    ```javascript
       import { Component } from '@angular/core';
    
        @Component({
          selector: 'app-root',
          template: `<nav>
                      <a routerLink="/signin" routerLinkActive="active">SignIn</a>
                      <a routerLink="/signup" routerLinkActive="active">SignUp</a>
                    </nav>  
                    <router-outlet></router-outlet>`,
          styleUrls: ['./app.component.css']
        })
        export class AppComponent {
          
        }
    
    ```
</details>
