package waxa.pruebapeticionesbyt;

import android.app.Activity;
import android.content.Intent;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;


public class MainActivity extends Activity {

    private Button registro;
    private Button login;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        registro = (Button)findViewById(R.id.registro);
        login = (Button)findViewById(R.id.login);

        registro.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                lanzarRegistro();
            }
        });

        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                lanzarLogin();
            }
        });
    }

    private void lanzarRegistro(){
        Intent i = new Intent(this, Registro.class);
        startActivity(i);
    }

    private void lanzarLogin(){
        Intent i = new Intent(this, Login.class);
        startActivity(i);
    }

}
