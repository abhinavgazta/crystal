package com.mygdx.game;

import android.content.Intent;
import android.os.Bundle;

import android.widget.Toast;
import com.badlogic.gdx.backends.android.AndroidApplication;
import com.badlogic.gdx.backends.android.AndroidApplicationConfiguration;

public class AndroidLauncher extends AndroidApplication {
    private int backButtonCount = 0;
	@Override
	protected void onCreate (Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		AndroidApplicationConfiguration config = new AndroidApplicationConfiguration();
        config.useAccelerometer = false;
        config.useCompass = false;

        Intent myIntent = getIntent();


        String actionKey = myIntent.getAction();
        switch (actionKey) {
            case "1":
                initialize(new Drop(), config);
                break;
            case "2":
                initialize(new DropLevelTwo(), config);
                break;
        }
		//initialize(new MyGdxGame(), config);
        //initialize(new Drop(), config);
	}

    @Override
    public void onBackPressed() {
        super.onBackPressed();
//        if(backButtonCount >= 1)
//        {
//            Intent intent = new Intent(Intent.ACTION_MAIN);
//            intent.addCategory(Intent.CATEGORY_HOME);
//            intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
//            startActivity(intent);
//        }
//        else
//        {
//            Toast.makeText(this, "Press the back button once again to close the application.", Toast.LENGTH_SHORT).show();
//            backButtonCount++;
//        }
    }
}
