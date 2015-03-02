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
    private Button nuevoPro;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        registro = (Button)findViewById(R.id.registro);
        login = (Button)findViewById(R.id.login);
        nuevoPro = (Button)findViewById(R.id.nuevoPro);

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

        nuevoPro.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                lanzarNuevoPro();
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

    private void lanzarNuevoPro(){
        Intent i = new Intent(this, NuevoPro.class);
        startActivity(i);
    }

}
