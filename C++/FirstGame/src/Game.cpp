#include "Game.h"
#include "SimpleObj.h"

Game::Game() {
    OGLES.Init(); // make sure we initialise the OGL instance we called OGLES
};
Game::~Game() {};// TODO: close some things down

void Game::Update()
{
    SimpleObj Bobby1;
    SimpleObj Bobby2;

    Bobby1.m_MyName = "Bobby1";
    Bobby2.m_MyName = "Bobby2";
    Bobby2.Xpos = 0.2f;

    // they do a draw, so they need to know where the Program Object is which is in OGLES
	Bobby1.ProgramObject = OGLES.programObject;
	Bobby2.ProgramObject = OGLES.programObject; // set up the program object

    for(int i=0; i<200; i++) {
        Bobby1.Update();
        Bobby2.Update();

        // the Bobbies have updated and drawn their triangle at the right position, but they are currently
// all drawn and held in a surface buffer, so now lets tell EGL to swap that buffer to the display so we can see it.
		eglSwapBuffers(OGLES.state.display, OGLES.state.surface);
    }
    return;
}
