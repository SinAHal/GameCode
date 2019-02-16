#pragma once
// Aks the compiler to include a header file only a single time, no matter how many times it has been imported
#include "OGL.h"

class Game
{
    public:
        Game();
        ~Game();
        void Update();
        OGL	OGLES;
};
