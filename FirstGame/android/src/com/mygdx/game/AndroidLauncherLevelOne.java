package com.mygdx.game;

import android.os.Bundle;
import com.badlogic.gdx.backends.android.AndroidApplicationConfiguration;

/**
 * Created by abhinavgazta on 6/11/16.
 */
public class AndroidLauncherLevelOne extends  AndroidLauncher {

    @Override
    protected void onCreate (Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        AndroidApplicationConfiguration config = new AndroidApplicationConfiguration();
        config.useAccelerometer = false;
        config.useCompass = false;
        //initialize(new MyGdxGame(), config);
        initialize(new Drop(), config);
    }

}
