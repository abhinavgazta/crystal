package com.mygdx.game;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;


public class LevelActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_level);
        final Intent launchLevelOne = new Intent(this, AndroidLauncher.class);
        final Intent launchLevelTwo = new Intent(this, AndroidLauncher.class);
        final Intent launchLevelThree = new Intent(this, AndroidLauncher.class);
        final Intent launchLevelFour = new Intent(this, AndroidLauncher.class);
        final Intent launchLevelFive = new Intent(this, AndroidLauncher.class);

        launchLevelOne.putExtra("levelone", "firstLevel");
        launchLevelOne.setAction("1");
        launchLevelTwo.setAction("2");
        launchLevelTwo.putExtra("leveltwo", "secondLevel");
        launchLevelThree.putExtra("levelthree", "thirdLevel");
        launchLevelFour.putExtra("levelFour", "fourthLevel");
        launchLevelFive.putExtra("levelFive", "fifthLevel");

        Button btn = (Button) findViewById(R.id.levelone);
        Button btnLevelTwo = (Button) findViewById(R.id.leveltow);
        Button btnLevelThree = (Button) findViewById(R.id.levelthree);
        Button btnLevelFour = (Button) findViewById(R.id.levelfour);
        Button btnLevelFive = (Button) findViewById(R.id.levelfive);


        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(launchLevelOne);
            }
        });
        btnLevelTwo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(launchLevelTwo);
            }
        });
        btnLevelThree.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(launchLevelThree);
            }
        });
        btnLevelFour.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(launchLevelFour);
            }
        });
        btnLevelFive.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(launchLevelFive);
            }
        });


    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_level, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
